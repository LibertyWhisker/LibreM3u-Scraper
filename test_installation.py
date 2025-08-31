#!/usr/bin/env python3
"""
Test script to verify M3U Scraper installation
"""

import sys
import importlib
import os

def test_imports():
    """Test that all required modules can be imported"""
    required_modules = [
        'requests',
        'json',
        'os',
        'sys',
        'datetime',
        'typing',
        'logging',
        'getpass'
    ]
    
    print("🔍 Testing module imports...")
    
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"  ✅ {module}")
        except ImportError as e:
            print(f"  ❌ {module}: {e}")
            return False
    
    return True

def test_local_imports():
    """Test that local modules can be imported"""
    print("\n🔍 Testing local module imports...")
    
    # Add src directory to path
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    sys.path.insert(0, src_path)
    
    try:
        from robust_iptv_scraper import RobustIPTVScraper
        print("  ✅ robust_iptv_scraper")
    except ImportError as e:
        print(f"  ❌ robust_iptv_scraper: {e}")
        return False
    
    try:
        from main import M3UScraperApp
        print("  ✅ main")
    except ImportError as e:
        print(f"  ❌ main: {e}")
        return False
    
    return True

def test_file_structure():
    """Test that required files exist"""
    print("\n🔍 Testing file structure...")
    
    required_files = [
        'src/main.py',
        'src/robust_iptv_scraper.py',
        'requirements.txt',
        'docs/README.md'
    ]
    
    for file in required_files:
        try:
            with open(file, 'r') as f:
                print(f"  ✅ {file}")
        except FileNotFoundError:
            print(f"  ❌ {file} (not found)")
            return False
    
    return True

def test_directories():
    """Test that required directories exist"""
    print("\n🔍 Testing directory structure...")
    
    required_dirs = [
        'src',
        'docs',
        'logs',
        'output',
        'examples',
        'temp'
    ]
    
    for directory in required_dirs:
        if os.path.isdir(directory):
            print(f"  ✅ {directory}/")
        else:
            print(f"  ❌ {directory}/ (not found)")
            return False
    
    return True

def main():
    """Run all tests"""
    print("🧪 M3U Scraper Installation Test")
    print("=" * 40)
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
    
    # Test local imports
    if not test_local_imports():
        all_passed = False
    
    # Test file structure
    if not test_file_structure():
        all_passed = False
    
    # Test directories
    if not test_directories():
        all_passed = False
    
    print("\n" + "=" * 40)
    if all_passed:
        print("✅ All tests passed! Installation is ready.")
        print("\n🚀 You can now run the application with:")
        print("   ./run.sh")
        print("   or")
        print("   cd src && python3 main.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 