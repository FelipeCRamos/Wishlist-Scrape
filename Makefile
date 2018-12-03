all:
	@ln -sfv src/main.py pcalc.py
	@chmod +x pcalc.py

clean:
	@rm -rf pcalc.py
