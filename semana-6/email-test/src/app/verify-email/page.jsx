"use client";

import { useSearchParams } from "next/navigation";
import { useState, useEffect } from "react";
import { CheckCircle, XCircle, Loader2, Mail, ArrowRight } from "lucide-react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Alert, AlertDescription } from "@/components/ui/alert";

export default function VerifyEmail() {
  const params = useSearchParams();
  const [success, setSuccess] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  const handleValidateToken = async () => {
    try {
      setIsLoading(true);
      const response = await fetch(
        "http://127.0.0.1:8000/api/v1/auth/verify-email/",
        {
          headers: {
            "Content-Type": "application/json",
          },
          method: "POST",
          body: JSON.stringify({ token: params.get("token") }),
        }
      );

      setSuccess(response.ok);
    } catch (error) {
      setSuccess(false);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    if (params.get("token")) {
      handleValidateToken();
    } else {
      setSuccess(false);
      setIsLoading(false);
    }
  }, [params]);

  const handleReturnToLogin = () => {
    // Navigate to login page - you can implement this based on your routing
    window.location.href = "/";
  };

  const handleResendEmail = () => {
    // Implement resend email functionality
    console.log("Resend email functionality");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <Card className="shadow-xl border-0 bg-white/80 backdrop-blur-sm">
          <CardHeader className="text-center pb-4">
            <div className="mx-auto mb-4 w-16 h-16 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-full flex items-center justify-center">
              <Mail className="w-8 h-8 text-white" />
            </div>
            <CardTitle className="text-2xl font-bold text-gray-900">
              Verificación de Email
            </CardTitle>
            <CardDescription className="text-gray-600 mt-2">
              Estamos verificando tu dirección de correo electrónico
            </CardDescription>
          </CardHeader>

          <CardContent className="space-y-6">
            {isLoading ? (
              <div className="text-center py-8">
                <Loader2 className="w-12 h-12 animate-spin text-blue-500 mx-auto mb-4" />
                <h3 className="text-lg font-semibold text-gray-900 mb-2">
                  Verificando...
                </h3>
                <p className="text-gray-600 text-sm">
                  Por favor espera mientras verificamos tu cuenta
                </p>
              </div>
            ) : success ? (
              <div className="text-center py-4">
                <div className="mx-auto mb-4 w-16 h-16 bg-green-100 rounded-full flex items-center justify-center">
                  <CheckCircle className="w-10 h-10 text-green-600" />
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-2">
                  ¡Cuenta Verificada Exitosamente!
                </h3>
                <p className="text-gray-600 mb-6">
                  Tu dirección de email ha sido confirmada. Ya puedes iniciar
                  sesión con tu cuenta.
                </p>

                <Alert className="mb-4 border-green-200 bg-green-50">
                  <CheckCircle className="h-4 w-4 text-green-600" />
                  <AlertDescription className="text-green-800">
                    Tu cuenta está ahora completamente activada y lista para
                    usar.
                  </AlertDescription>
                </Alert>

                <Button
                  onClick={handleReturnToLogin}
                  className="w-full bg-gradient-to-r from-blue-500 to-indigo-600 hover:from-blue-600 hover:to-indigo-700 text-white font-medium py-2.5"
                >
                  Ir al Inicio de Sesión
                  <ArrowRight className="w-4 h-4 ml-2" />
                </Button>
              </div>
            ) : (
              <div className="text-center py-4">
                <div className="mx-auto mb-4 w-16 h-16 bg-red-100 rounded-full flex items-center justify-center">
                  <XCircle className="w-10 h-10 text-red-600" />
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-2">
                  Error de Verificación
                </h3>
                <p className="text-gray-600 mb-6">
                  No se pudo activar la cuenta. El enlace puede haber expirado o
                  ser inválido.
                </p>

                <Alert className="mb-6 border-red-200 bg-red-50">
                  <XCircle className="h-4 w-4 text-red-600" />
                  <AlertDescription className="text-red-800">
                    El token de verificación no es válido o ha expirado. Por
                    favor, solicita un nuevo enlace de verificación.
                  </AlertDescription>
                </Alert>

                <div className="space-y-3">
                  <Button
                    onClick={handleResendEmail}
                    className="w-full bg-gradient-to-r from-blue-500 to-indigo-600 hover:from-blue-600 hover:to-indigo-700 text-white font-medium py-2.5"
                  >
                    Reenviar Email de Verificación
                    <Mail className="w-4 h-4 ml-2" />
                  </Button>

                  <Button
                    variant="outline"
                    onClick={handleReturnToLogin}
                    className="w-full border-gray-300 text-gray-700 hover:bg-gray-50 bg-transparent"
                  >
                    Volver al Inicio de Sesión
                  </Button>
                </div>
              </div>
            )}
          </CardContent>
        </Card>

        <div className="text-center mt-6">
          <p className="text-sm text-gray-500">
            ¿Necesitas ayuda?{" "}
            <a
              href="/support"
              className="text-blue-600 hover:text-blue-700 font-medium"
            >
              Contacta soporte
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}
