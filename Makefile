# Author: FelipeCRamos

# Prepare ambient for the program
all:
	@ln -sfv src/main.py pcalc.py
	@chmod +x pcalc.py
	@mkdir -p logs
	@echo "Everything ready, just run:\n./pcalc.py [input_file] [kabum/mercadolivre]"

# Clean dirty files
clean:
	@rm -rf pcalc.py
	@rm -rf src/sites/__pycache__
	@rm -rf src/__pycache__
	@echo "Cleanup done!"

# Clean logs generated
clogs:
	@rm -rf logs/*
	@echo "Logs cleaned!"
