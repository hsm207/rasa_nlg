run-rasa-server:
	rasa run -vv \
		--enable-api \
		--cors "*" \
		-m models \
		--credentials credentials.yml

run-rasa-server-no-nlg:
	rasa run -vv \
		--enable-api \
		--cors "*" \
		-m models \
		--credentials credentials.yml \
		--endpoints /dev/null

run-nlg-server:
	uvicorn server.nlg:app --host 127.0.0.1 \
		--port 8000