#!/usr/bin/env python3
"""
Simple HTTP server for serving the Korean quiz game about 기욱.
Serves static files including HTML, CSS, JS, and audio files.
"""

import http.server
import socketserver
import os
import mimetypes
from urllib.parse import urlparse

class QuizGameHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler for the quiz game with proper MIME types and CORS headers."""
    
    def __init__(self, *args, **kwargs):
        # Add custom MIME types for audio files
        mimetypes.add_type('audio/wav', '.wav')
        mimetypes.add_type('audio/mpeg', '.mp3')
        super().__init__(*args, **kwargs)
    
    def end_headers(self):
        # Add CORS headers for better compatibility
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        """Handle GET requests with custom routing."""
        parsed_path = urlparse(self.path)
        path = parsed_path.path.lstrip('/')
        
        # Serve index.html for root path
        if path == '' or path == '/':
            path = 'index.html'
        
        # Check if file exists
        if os.path.exists(path) and os.path.isfile(path):
            super().do_GET()
        else:
            # Return 404 for missing files
            self.send_error(404, f"File not found: {path}")
    
    def log_message(self, format, *args):
        """Custom log format for better readability."""
        print(f"[Quiz Server] {self.address_string()} - {format % args}")

def main():
    """Start the quiz game server."""
    PORT = 5000
    HOST = '0.0.0.0'
    
    print(f"🎯 Starting 기욱 Quiz Game Server...")
    print(f"📍 Server running at http://{HOST}:{PORT}")
    print(f"🎮 Access the quiz at http://localhost:{PORT}")
    print(f"📁 Serving files from: {os.getcwd()}")
    
    # Check if required files exist
    required_files = ['index.html']
    for file_path in required_files:
        if not os.path.exists(file_path):
            print(f"⚠️  Warning: Required file '{file_path}' not found!")
    
    # Check audio directory
    audio_dir = 'audio'
    if os.path.exists(audio_dir):
        audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.wav')]
        print(f"🎵 Found {len(audio_files)} audio files in {audio_dir}/")
    else:
        print(f"⚠️  Audio directory '{audio_dir}' not found. Audio features may not work.")
    
    try:
        with socketserver.TCPServer((HOST, PORT), QuizGameHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")

if __name__ == "__main__":
    main()
