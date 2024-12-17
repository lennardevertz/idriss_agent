"""Custom exceptions for the project."""


class BadRequestError(Exception):
    """Exception raised for bad requests (HTTP 400)."""
    pass


class UnauthorizedError(Exception):
    """Exception raised for unauthorized access (HTTP 401)."""
    pass


class ForbiddenError(Exception):
    """Exception raised for forbidden actions (HTTP 403)."""
    pass


class NotFoundError(Exception):
    """Exception raised when a resource is not found (HTTP 404)."""
    pass


class ConflictError(Exception):
    """Exception raised for conflicts (HTTP 409)."""
    pass


class ValidationError(Exception):
    """Exception raised for validation errors (HTTP 422)."""
    pass


class InternalServerError(Exception):
    """Exception raised for internal server errors (HTTP 500)."""
    pass


class ServiceUnavailableError(Exception):
    """Exception raised when the service is unavailable (HTTP 503)."""
    pass