# Author: FelipeCRamos

# Prepare ambient for the program
all:
	@ln -sfv src/main.py wcalc.py
	@chmod +x wcalc.py
	@mkdir -p logs
	@echo "Everything ready, just run:\n./wcalc.py [input_file] [output_file]"

# Clean dirty files
clean:
	@rm -rf wcalc.py
	@rm -rf src/sites/__pycache__
	@rm -rf src/__pycache__
	@echo "Cleanup done!"

# Clean logs generated
clogs:
	@rm -rf logs/*
	@echo "Logs cleaned!"
