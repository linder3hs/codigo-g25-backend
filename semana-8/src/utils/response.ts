import type { Response } from "express";

// Generic type
export function sendSuccess<T>(
  response: Response,
  message: string,
  data?: T,
  statusCode: number = 200
) {
  const res = {
    success: true,
    message,
    data,
  };

  response.status(statusCode).json(res);
}

export function sendError(
  response: Response,
  message: string,
  statusCode: number = 500,
  error?: string
) {
  const res = {
    success: false,
    message,
    error,
  };
  response.status(statusCode).json(res);
}
