import requests
from typing import Optional, Dict, Any

class ApiClient:
    """Статический класс для выполнения HTTP-запросов."""
    @staticmethod
    def _send_request(
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        expected_status: Optional[int] = None,
        log: bool = True
    ) -> requests.Response:
        if log:
            print(f"[{method}] {url}")  # Нужно заменить на logging
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json_data
        )
        if expected_status is not None:
            assert response.status_code == expected_status, (
                f"Ожидался статус {expected_status}, получен {response.status_code}"
            )
        return response

    @staticmethod
    def get(
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        expected_status: int = 200,
        log: bool = True
    ) -> requests.Response:
        """GET-запрос."""
        return ApiClient._send_request(
            method="GET",
            url=url,
            headers=headers,
            params=params,
            expected_status=expected_status,
            log=log
        )