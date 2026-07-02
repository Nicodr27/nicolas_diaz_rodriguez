Inicio
  Leer Emisor
  Leer Beneficiario
  Leer Monto en pesos chilenos

  // Conversión de monedas
  Dólares := Monto * TipoCambioUSD
  Bolívares := Monto * TipoCambioVES
  Euros := Monto * TipoCambioEUR

  // Calcular comisión
  Comision := Monto * 0.001   // 0,10 %
  MontoFinal := Monto - Comision

  // Mostrar resultados
  Imprimir "Emisor: ", Emisor
  Imprimir "Beneficiario: ", Beneficiario
  Imprimir "Monto original en CLP: ", Monto
  Imprimir "Monto en USD: ", Dólares
  Imprimir "Monto en VES: ", Bolívares
  Imprimir "Monto en EUR: ", Euros
  Imprimir "Comisión aplicada: ", Comision
  Imprimir "Monto final: ", MontoFinal

  // Generar comprobante
  Guardar comprobante en base de datos
  Mostrar comprobante al usuario en su sesión

  // Flujo de aprobación
  Si Validación exitosa entonces
      Mostrar "Solicitud aprobada"
  Si no
      Mostrar "Solicitud rechazada"
Fin

