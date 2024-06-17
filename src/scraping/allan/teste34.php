<?php

// Função para realizar o scraping
function syngenta_temp_vento($city) {
    // URL da página alvo
    $url = 'https://www.syngenta.pt/ajax/weather/services/weather-widgets-update';

    // Parâmetros da requisição POST
    $data = http_build_query(array(
        'locationName' => $city.', Portugal',
        'synWeatherSettings[fromDate]' => date('Y-m-d'),
        'synWeatherSettings[sprayWindowHourlyEnabled]' => '1',
        'synWeatherSettings[showEightHourlyImages]' => '1',
        'synWeatherSettings[showPredictability]' => '1',
        'synWeatherSettings[showMoreDays]' => 'false',
        'synWeatherSettings[toDate]' => 'today + 7 days - 1 second',
        'widgets[]' => 'weather-widget-1718581609::weather_graph',
        'widgets[]' => 'weather-widget-1718580407--2::weather_daily',
        'widgets[]' => 'weather-widget-1718580407--4::weather_hourly',
    ));

    // Configuração da requisição cURL
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        'accept: */*',
        'accept-language: pt-BR,pt;q=0.9',
        'content-type: application/x-www-form-urlencoded; charset=UTF-8',
        'cookie: cf_clearance=7MrPEUbnLONYGJSpDN9L_rW5Cv_FtbzoevKw9c6YfE0-1718580161-1.0.1.1-cmZ9rwM5jhj15kgzgVvtNHYi6b.sikEvRYiXkYMFj3e2PpV_UkvHpTodHJHKB8UYM7yvnb_og3g5F0oorYmOag; SSESS01050bbd327529cb5f3bde04c42f63a8=h%2CdKHTJ7P96poqVzQjD4wA3vB3dGG2MXwLq22OLl3cTMfXCG; __cf_bm=zG_TyPYcho52PAA8V7GfSoLasoXddCDJqqkuAUw1AFs-1718581603-1.0.1.1-_.Js4oTulCNCnmE._iWfUmU8jeTGvVIDPDIQaNWTdVIEzZJd0ZNhVBY2Pexkh5aGs1.UdtFypvTjaR0CH5s4mA',
        'origin: https://www.syngenta.pt',
        'priority: u=1, i',
        'referer: https://www.syngenta.pt/service/previsao-do-tempo',
        'sec-ch-ua: "Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile: ?0',
        'sec-ch-ua-model: ""',
        'sec-ch-ua-platform: "Linux"',
        'sec-ch-ua-platform-version: "6.1.0"',
        'sec-fetch-dest: empty',
        'sec-fetch-mode: cors',
        'sec-fetch-site: same-origin',
        'sec-gpc: 1',
        'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-requested-with: XMLHttpRequest',
    ));

    // Executar a requisição cURL e obter a resposta
    $response = curl_exec($ch);
    curl_close($ch);

    // Verificar se a requisição foi bem sucedida
    if ($response === false) {
        echo 'Erro ao realizar requisição cURL: ' . curl_error($ch);
        return;
    }

    // Decodificar a resposta JSON
    $json_response = json_decode($response, true);


    // Extrair dados relevantes da resposta
    $locationName = $json_response['locationName'];
    $weatherData = $json_response['weather'];

    // Aqui você pode processar e salvar os dados como desejar
    // Exemplo de exibição dos dados
    echo "Previsão do tempo para: $locationName\n";
    foreach ($weatherData as $day) {
        echo "Data: {$day['date']}\n";
        echo "Temperatura máxima: {$day['maxTemp']}\n";
        echo "Temperatura mínima: {$day['minTemp']}\n";
        echo "Condição do tempo: {$day['condition']}\n";
        echo "\n";
    }
}

// Exemplo de utilização
syngenta_temp_vento('Lisboa');

?>
