export interface CreateCategoryRequest {
  name: string;
  description?: string | null;
}

export interface UpdateCategoryRequest {
  name?: string;
  description?: string | null;
}

export interface CreateProductRequest {
  name: string;
  description?: string | null;
  categoryId?: number;
  price: number;
  stock: number;
}

export interface UpdateProductRequest {
  name?: string;
  description?: string;
  categoryId?: number;
  price?: number;
  stock?: number;
  isActive?: boolean;
}
