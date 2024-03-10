from fastapi import HTTPException, status


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

expired_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token expired",
)
