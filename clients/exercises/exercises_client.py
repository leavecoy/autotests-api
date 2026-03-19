from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, AuthenticationUserDict

class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение упражнения.
    """
    exercise: Exercise

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений курса.
    """
    courseId: str

class GetExercisesResponseDict(TypedDict):
    """
    Описание ответа на получение списка упражнений
    """
    exercises: list[Exercise]

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на создание упражнения.
    """
    exercise: Exercise

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на обновление упражнения.
    """
    exercise: Exercise

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений.
        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод получения списка упражнений.
        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта .json
        """
        response = self.get_exercises_api(query=query)
        return response.json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.
        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод получения упражнения.
        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта .json
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description и estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод создания упражнения.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description и estimatedTime.
        :return: Ответ от сервера в виде объекта .json
        """
        response = self.create_exercise_api(request=request)
        return response.json()

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения.
        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description и estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод обновления упражнения.
        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description и estimatedTime.
        :return: Ответ от сервера в виде объекта .json
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return response.json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метода удаления упражнения.
        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(get_private_http_client(user=user))