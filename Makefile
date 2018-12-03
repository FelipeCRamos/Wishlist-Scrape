all:
	@ln -sfv src/main.py pcalc.py
	@chmod +x pcalc.py
	@echo "Everything ready, just run:\n./pcalc.py [input_file] [kabum/mercadolivre]"

clean:
	@rm -rf pcalc.py
	@rm -rf src/sites/__pycache__
	@rm -rf src/__pycache__
	@echo "Cleanup done!"

clean_logs:
	@rm -rf logs/*
	@echo "Logs cleaned!"
