## 0.3.0 (2024-09-07)

### Feat

- **src/domain/validators**: add EmailAvailableValidator interface
- **src/domain/usecases**: add RegisterUserUseCase interface
- **src/data/usecases**: add implementation for register user use case
- **src/data/protocols/repositories**: add GetUserByEmailRepository interface
- **src/data/protocols/cryptography**: add Hasher interface

### Refactor

- **src/domain/models**: remove name field from User model
- **src/domain/models**: update BaseEntity datetime fields

## 0.2.0 (2024-09-07)

### Feat

- **src/domain/models**: add entity base and user entity

## 0.1.1 (2024-09-07)

### Refactor

- **src/auth/__init__.py**: remove a unused file
