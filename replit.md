# ⚓ 기욱 지식왕 퀴즈

## Overview

This is a Korean quiz game application about a character named "기욱" (Gi-ook). The application is a single-page web game that presents quiz questions about this character and provides personalized results based on the user's score. The game features a dark-themed UI with progress tracking, multiple choice questions, and character-specific endings delivered as direct quotes from 기욱.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Single-page application**: Built as a standalone HTML file with embedded CSS and JavaScript
- **Responsive design**: Uses CSS Grid/Flexbox with mobile-first approach
- **Dark theme**: Implements a custom dark color scheme with CSS custom properties
- **Component-based styling**: Modular CSS classes for cards, buttons, modals, and interactive elements
- **Progressive quiz flow**: Handles question progression, score tracking, and result display

### UI/UX Design Patterns
- **Card-based layout**: Main content contained within a centered card component
- **Modal system**: Overlay modals for help/information display
- **Interactive feedback**: Visual feedback for correct/incorrect answers with color coding
- **Progress indication**: Visual progress bar showing quiz completion status

### Game Logic Architecture
- **Score-based results**: Quiz outcomes determined by performance percentage
- **Character-driven endings**: Results delivered as direct quotes from the 기욱 character
- **Optional AI integration**: Configurable AI-generated responses based on character lore
- **Audio support**: Optional sound effects and voice responses for different score ranges

### Content Management
- **Static content delivery**: All quiz questions, answers, and character data embedded in the application
- **Localized interface**: Korean language support throughout the application
- **Character lore system**: Background information about 기욱 used for contextual responses

## External Dependencies

### Server Infrastructure
- **Python HTTP server**: Simple static file server (`server.py`) with custom MIME type handling
- **CORS support**: Cross-origin resource sharing headers for better compatibility
- **Static asset serving**: Handles HTML, CSS, JavaScript, and audio file delivery

### Optional Integrations
- **AI service integration**: Configurable connection to AI services for dynamic response generation
- **Audio file support**: WAV and MP3 file handling for sound effects and voice responses
- **Font integration**: System fonts with fallback to "Noto Sans KR" for Korean text support

### Browser Requirements
- **Modern browser support**: Requires support for CSS custom properties, Flexbox, and ES6 JavaScript
- **Audio API support**: Optional Web Audio API for sound playback features
- **Modal backdrop support**: CSS backdrop-filter for modal overlay effects