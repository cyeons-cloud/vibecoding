# 한국어 N행시 생성기

## Overview

This is a Korean acrostic poem generator web application built with Streamlit and Google's Gemini AI. The application allows users to input Korean words and generates creative N-line poems (N행시) where each line starts with the corresponding character from the input word. The app features a clean, user-friendly interface with Korean language support and real-time poem generation capabilities.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit web framework for rapid prototyping and deployment
- **UI Components**: Centered layout with expandable help sections, input validation, and responsive design
- **Language Support**: Full Korean language interface with UTF-8 character validation
- **User Experience**: Step-by-step guidance with examples and error handling for invalid inputs

### Backend Architecture
- **Core Logic**: Modular design with separated concerns between UI (app.py) and AI integration (gemini_client.py)
- **AI Integration**: Google Gemini API client for natural language generation
- **Input Processing**: Character-level analysis of Korean words with validation for Hangul characters
- **Error Handling**: Comprehensive validation for API keys, input format, and word length constraints

### Configuration Management
- **Environment Variables**: API key management through environment variables for security
- **Input Constraints**: Word length limits (2-10 characters) and Korean character validation
- **Page Configuration**: Streamlit page settings with custom title, icon, and layout

### Prompt Engineering
- **System Prompts**: Structured prompts with specific formatting rules for consistent output
- **Content Guidelines**: Rules for positive, meaningful content with proper line length and formatting
- **Output Format**: Standardized bracket notation for each line starting character

## External Dependencies

### AI Services
- **Google Gemini AI**: Primary language model for poem generation via google.genai client
- **API Authentication**: Requires GEMINI_API_KEY environment variable

### Python Frameworks
- **Streamlit**: Web application framework for the user interface
- **Standard Library**: os module for environment variable access, logging for error tracking

### Language Processing
- **Unicode Support**: Korean character validation using Unicode ranges (가-힣)
- **Character Analysis**: Built-in Python string processing for Hangul text manipulation