import prisma from "../config/database";

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
}
