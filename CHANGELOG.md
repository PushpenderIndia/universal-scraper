# Changelog

All notable changes to this project will be documented in this file.

## v1.9.3 - MCP Server Integration Release
- **NEW**: Model Context Protocol (MCP) server implementation
- **ARCHITECTURE**: Complete MCP server infrastructure with async stdio transport
- **INTEGRATION**: Native Claude Code and MCP-compatible AI client support
- **TOOLS**: MCP tool interface for scrape_url, scrape_multiple_urls, configure_scraper operations
- **DEPLOYMENT**: Standalone MCP server entry point with console script integration
- **VALIDATION**: Input validation and error handling for MCP tool calls
- **DOCS**: Claude Code integration documentation and setup guides

## v1.9.2 - URL Optimization & Refactoring Release
- **NEW**: URL placeholder replacement - replaces long URLs (src, href, action) with short placeholders like `[IMG_URL]`, `[LINK_URL]` to reduce token count
- **REFACTOR**: Complete HTML cleaner modularization - split monolithic 1240+ line file into 8 focused components
- **ARCHITECTURE**: New modular structure with `browsegenie/core/cleaning/` package containing specialized modules:
  - `base_cleaner.py` - Common utilities and configuration
  - `noise_remover.py` - Scripts, styles, comments, SVG, iframe removal
  - `url_replacer.py` - **NEW: URL placeholder replacement functionality**
  - `structure_cleaner.py` - Headers/footers removal and main content focus
  - `content_optimizer.py` - Text collapsing, empty divs, whitespace optimization
  - `duplicate_finder.py` - Repeating structures detection and removal
  - `attribute_cleaner.py` - Non-essential attributes removal
  - `html_cleaner.py` - Main orchestrator coordinating all cleaning steps
- **PERFORMANCE**: URL replacement provides additional token savings on URL-heavy pages
- **MAINTAINABILITY**: Each module now has single responsibility (~150-300 lines vs 1240+ monolith)
- **TESTABILITY**: Modular components can be tested and modified independently
- **DOCS**: Updated README with URL replacement step in mermaid diagram and feature description
- **COMPATIBILITY**: Full backward compatibility maintained - existing imports continue to work
- **SMART**: Intelligent URL placeholder selection based on element type (IMG_URL, LINK_URL, FORM_URL, etc.)
- **LOGGING**: Added URL replacement statistics and improved cleaning pipeline logging

## v1.9.1 - Patch Release
- 🐛 **FIX**: Minor bug fixes and improvements

## v1.9.0 - Testing & SVG Optimization Release
- NEW: Inline SVG image remover - removes embedded SVG images to reduce HTML size
- TESTING: Added comprehensive test suite with 105 test cases for intensive testing
- ENHANCEMENT: Improved code coverage and reliability
- MAINTENANCE: Removed unused dependencies for cleaner codebase
- CI/CD: Updated GitHub workflows and removed Python 3.8 support

## v1.8.0 - Advanced HTML Optimization Release
- 🚀 **NEW**: Non-essential attributes removal - removes styling, tracking, and testing attributes while preserving data extraction capabilities
- 🧹 **NEW**: Whitespace compression between consecutive HTML tags - removes unnecessary whitespace and newlines between tags
- 🎯 **FEATURE**: Smart attribute filtering - distinguishes between essential attributes (id, class, href, data-price) and non-essential ones (style, onclick, data-analytics)
- 📦 **OPTIMIZATION**: Additional 15-30% HTML size reduction through attribute cleanup
- ⚡ **PERFORMANCE**: Enhanced token savings with dual whitespace and attribute optimization
- 🔧 **SMART**: Preserves BeautifulSoup selector attributes (class, id) while removing presentation attributes
- 📊 **LOGGING**: Detailed attribute removal statistics and whitespace compression metrics
- 🛠️ **PIPELINE**: Integrated as steps 7-8 in the cleaning pipeline for maximum efficiency

## v1.7.0 - HTML Form Optimization Release
- 🔧 **NEW**: Select options limiting - automatically reduces select tags to maximum 2 options
- 🧹 **ENHANCEMENT**: Improved HTML cleaning with form element optimization
- 📦 **OPTIMIZATION**: Further reduces HTML size by removing excessive form options
- 🎯 **FEATURE**: Smart form simplification preserves essential functionality while reducing complexity
- ⚡ **PERFORMANCE**: Reduced token usage in AI processing through cleaner HTML forms

## v1.6.0 - Enhanced CLI with Full Multi-Provider Support Release
- 🚀 **NEW**: Complete CLI rewrite with LiteLLM multi-provider support
- 🔧 **NEW**: CLI now supports OpenAI, Anthropic, and 100+ other AI models  
- 📝 **NEW**: `--api-key` and `--model` CLI arguments for any provider
- 🎯 **NEW**: `--fields` CLI argument for custom field extraction
- 🔄 **ENHANCEMENT**: Dynamic help examples showing `browsegenie` instead of `python main.py`
- 📋 **ENHANCEMENT**: Better CLI error handling and user feedback
- 🌍 **ENHANCEMENT**: Environment variable auto-detection in CLI
- 🛠️ **API**: Backward compatible - existing CLI usage still works
- ⚡ **PERFORMANCE**: CLI now uses same optimized pipeline as Python API

## v1.5.0 - Multi-Provider AI Support Release
- 🚀 **NEW**: LiteLLM integration for 100+ AI models support
- 🤖 **NEW**: Support for OpenAI GPT models (gpt-4, gpt-3.5-turbo, etc.)
- 🧠 **NEW**: Support for Anthropic Claude models (claude-3-opus, claude-3-sonnet, claude-3-haiku)
- 🔧 **NEW**: Automatic provider detection based on API key patterns
- 🔧 **NEW**: Environment variable auto-detection (OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY)
- 📝 **FEATURE**: Flexible model switching with `set_model_name()` method
- 🔄 **ENHANCEMENT**: Backward compatibility maintained - Gemini remains default
- 📚 **DOCS**: Comprehensive multi-provider usage examples and setup guides
- ⚡ **API**: Updated all methods to work seamlessly with any supported AI provider

## v1.4.0 - CSV Export Support Release
- 📊 **NEW**: CSV export functionality with `format='csv'` parameter
- 📈 **NEW**: Support for both JSON (default) and CSV output formats
- 🔧 **NEW**: CLI `--format` flag for choosing output format
- 📋 **FEATURE**: Automatic field detection and consistent CSV structure
- 🔄 **FEATURE**: Universal data format compatibility (Excel, Google Sheets, pandas)
- 📝 **DOCS**: Comprehensive CSV export documentation with examples
- 🛠️ **API**: Updated all scraping methods to support format parameter
- ✨ **ENHANCEMENT**: JSON remains the default format for backward compatibility

## v1.2.0 - Smart Caching & HTML Optimization Release
- 🚀 **NEW**: Intelligent code caching system - **saves 90%+ API tokens**
- 🧹 **HIGHLIGHT**: Smart HTML cleaner reduces payload by 91%+ - **massive token savings**
- 🔧 **NEW**: Structural HTML hashing for cache key generation
- 🔧 **NEW**: SQLite-based cache storage with metadata
- 🔧 **NEW**: Cache management methods: `get_cache_stats()`, `clear_cache()`, `cleanup_old_cache()`
- 🔧 **NEW**: Automatic cache hit/miss detection and logging  
- 🔧 **NEW**: URL normalization (removes query params) for better cache matching
- ⚡ **PERF**: 5-10x faster scraping on cached HTML structures
- 💰 **COST**: Significant API cost reduction (HTML cleaning + caching combined)
- 📁 **ORG**: Moved sample code to `sample_code/` directory

## v1.1.0
- ✨ **NEW**: Gemini model selection functionality
- 🔧 Added `model_name` parameter to `BrowseGenie()` constructor
- 🔧 Added `get_model_name()` and `set_model_name()` methods
- 🔧 Enhanced convenience `scrape()` function with `model_name` parameter  
- 🔄 Updated default model to `gemini-2.5-flash`
- 📚 Updated documentation with model examples
- ✅ Fixed missing `cloudscraper` dependency

## v1.0.0
- Initial release
- AI-powered field extraction
- Customizable field configuration
- Multiple URL support
- Comprehensive test suite