async function update_moneda(element_id, api_url) {
  let obj;

  const res = await fetch(api_url);

  obj = await res.json();

  console.log(obj);
  document.getElementById(element_id).innerHTML = obj['venta'];
}

update_moneda(
	element_id = 'precio_USD',
	api_url = 'https://dolarapi.com/v1/dolares/solidario',
);
update_moneda(
	element_id = 'precio_BRL',
	api_url = 'https://dolarapi.com/v1/cotizaciones/brl',
);
update_moneda(
	element_id = 'precio_EUR',
	api_url = 'https://dolarapi.com/v1/cotizaciones/eur',
);
