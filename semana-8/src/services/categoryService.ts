import prisma from "../config/database";
import { CreateCategoryRequest, UpdateCategoryRequest } from "../types";

/**
 * CREATE
 * READ
 * UPDATE
 * DELETE
 */

export class CategoryService {
  static async getAllCategories() {
    return await prisma.category.findMany();
  }

  // funcion para buscar una categoria por id
  static async getCategoryById(id: number) {
    return await prisma.category.findUnique({ where: { id } });
  }

  static async createCategory(data: CreateCategoryRequest) {
    return await prisma.category.create({ data });
  }

  static async updateCategory(id: number, data: UpdateCategoryRequest) {
    const category = await prisma.category.findUnique({ where: { id } });

    if (!category) return false;

    return await prisma.category.update({ where: { id }, data });
  }

  static async deleteCategory(id: number) {
    return await prisma.category.delete({ where: { id } });
  }
}
