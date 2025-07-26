import { Request, Response, NextFunction } from "express";
import { sendError } from "../utils/response";

export function errorHandler(
  error: Error,
  req: Request,
  res: Response,
  next: NextFunction
): void {
  console.error(error.stack);

  if (error.name === "ValidationError") {
    sendError(res, "Error de Validacion", 400, error.message);
    return;
  }

  if (error.name === "CastError") {
    sendError(res, "Id invalido", 400);
    return;
  }

  sendError(res, "Error interno del servidor", 500);
}

export function notFound(req: Request, res: Response): void {
  sendError(res, `Ruta ${req.originalUrl} not found`, 404);
}
