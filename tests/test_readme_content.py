"""
Tests for README.md content validation
"""
import os
import re


def test_readme_exists():
    """Test that README.md file exists in the root directory"""
    readme_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')
    assert os.path.exists(readme_path), "README.md file should exist in the root directory"


def test_readme_fre_cli_description_spelling():
    """Test that the fre-cli description contains correct spelling"""
    readme_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Test that the description contains the correct word "gives" not "gies"
    fre_cli_description_pattern = r'`fre-cli`.*aims.*to.*gives.*users.*intuitive'
    
    assert re.search(fre_cli_description_pattern, readme_content, re.IGNORECASE), \
        "README.md should contain correct spelling 'gives' in fre-cli description"
    
    # Explicitly check that the incorrect spelling "gies" is not present
    incorrect_pattern = r'`fre-cli`.*aims.*to.*gies.*users'
    
    assert not re.search(incorrect_pattern, readme_content, re.IGNORECASE), \
        "README.md should not contain the misspelled word 'gies' in fre-cli description"


def test_readme_contains_required_sections():
    """Test that README.md contains required sections and information"""
    readme_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Check for essential components
    assert 'fre-cli' in readme_content, "README should mention fre-cli"
    assert 'Flexible Runtime Environment' in readme_content, "README should mention Flexible Runtime Environment"
    assert 'command-line interface' in readme_content, "README should mention command-line interface"
    assert 'Documentation' in readme_content, "README should contain documentation link"


def test_readme_no_common_typos():
    """Test that README.md doesn't contain common typos in key descriptions"""
    readme_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # List of common typos to check for in the context of this project
    typos = ['gies', 'givs', 'comandline', 'comand-line', 'enviroment']
    
    for typo in typos:
        assert typo not in readme_content.lower(), f"README.md should not contain the typo '{typo}'"