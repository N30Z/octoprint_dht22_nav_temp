// js/dht22_nav_temp.js

$(function() {
    function updateNavbar() {
        $.ajax({
            url: "/api/plugin/dht22_nav_temp",
            type: "POST",
            dataType: "json",
            data: JSON.stringify({
                command: "get_data"
            }),
            contentType: "application/json; charset=UTF-8"
        }).done(function(data) {
            if (data) {
                $('[data-bind="temperature"]').text("Temperature: " + data.temperature.toFixed(1) + "°C");
                $('[data-bind="humidity"]').text("Humidity: " + data.humidity.toFixed(1) + "%");
            }
        }).fail(function() {
            console.error("Failed to fetch DHT22 data");
        });
    }

    updateNavbar();
    setInterval(updateNavbar, 1000 * parseInt(OctoPrint.coreui.settings.settings.plugins.dht22_nav_temp.refresh_rate));
});
