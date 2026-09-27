# Project context

Portfolio tests for the educational API Course service.
Stack: pytest, HTTPX, Pydantic v2, JSON Schema, Faker and Allure.

- clients/: transport, domain clients and request/response models.
- fixtures/: client and test-data setup.
- tests/: integration scenarios grouped by domain.
- tools/assertions/: reusable business and contract assertions.

Review actual code and requirements. Do not invent team policies or coverage
numbers. Distinguish defects from suggestions. Check HTTP statuses, resource
lifetime, test isolation, sensitive attachments and assertion quality.
