import type { Request, Response } from "express";
import type { UpdateCategoryRequest, CreateCategoryRequest } from "../types";
import { CategoryService } from "../services/categoryService";
import { sendError, sendSuccess } from "../utils/response";
/**
 * Create
 * Read
 * Update
 * Delete
 */

export class CategoryController {
  static async getAllCategories(req: Request, res: Response) {
    try {
      const result = await CategoryService.getAllCategories();

      sendSuccess(res, "Lista de Categorias", result);
    } catch (error) {
      sendError(
        res,
        "Error al crear un producto",
        500,
        error instanceof Error ? error.message : "Error Desconocido"
      );
    }
  }
}
