run_docker:
	docker-compose up -d

run_fastapi:
	uvicorn ACMEsports.main:app --reload