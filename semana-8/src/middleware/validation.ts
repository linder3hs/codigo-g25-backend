import type { Request, Response, NextFunction } from "express";
import { sendError } from "../utils/response";

export function validateProduct(
  req: Request,
  res: Response,
  next: NextFunction
): void {
  const { name, price, stock } = req.body;

  if (!name || name.trim() === "") {
    sendError(res, "El nombre del producto es requerido", 400);
  }

  if (!price || price <= 0) {
    sendError(res, "El precio debe ser mayor a 0", 400);
  }

  if (!stock || stock < 0) {
    sendError(res, "El stock no puede ser menor a 0");
    return;
  }

  next();
}
