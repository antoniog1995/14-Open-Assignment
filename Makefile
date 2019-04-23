.PHONY: doc test

doc: 
                pandoc README.md 
    
test: 
                python3 -m pytest -v test.py 
