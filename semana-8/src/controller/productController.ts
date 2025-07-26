import type { Request, Response } from "express";
import { ProductService } from "../services/productService";
import { sendSuccess, sendError } from "../utils/response";
import { CreateProductRequest } from "../types";

export class ProductController {
  static async getAllProduct(req: Request, res: Response): Promise<void> {
    try {
      const page = Number(req.query.page || "1");
      const limit = Number(req.query.limit || "10");
      const search = req.query.search as string;

      const result = await ProductService.getAllProduct(page, limit, search);

      sendSuccess(res, "Lista de productos", result);
    } catch (error) {
      sendError(
        res,
        "Error al obtener products",
        500,
        error instanceof Error ? error.message : "Error Desconocido"
      );
    }
  }

  static async createProduct(
    req: Request<{}, any, CreateProductRequest>,
    res: Response
  ): Promise<void> {
    try {
      const productData = req.body;
      const newProduct = await ProductService.createProduct(productData);

      sendSuccess<CreateProductRequest>(
        res,
        "Product creado existosamente",
        newProduct,
        201
      );
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
