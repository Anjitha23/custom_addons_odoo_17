/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.combineFilters = publicWidget.Widget.extend({
    selector: '.combo-filter',
    events: {
        'change': '_onChangeAttribute',
    },

    _onChangeAttribute: function (ev) {
        ev.preventDefault();
        // Update the URL with the selected combo_ids
        var form = $('#wsale_products_attributes_collapse').find('form');


        var url = new URL(window.location.href);
        var combos = []
        $('#products_grid_before .combo-filter:checked').each(function (index,element) {
            combos.push(element.value)
           $('<input>').attr({
            type: 'hidden',
            name: 'combo_products',
            value: element.value,
            }).appendTo(form);
        });
        var combo_set = new Set(combos)
        var combo_array = [...combo_set];
        url.searchParams.set('combo_products', combo_array)
        window.location.href = url;
    },
});
