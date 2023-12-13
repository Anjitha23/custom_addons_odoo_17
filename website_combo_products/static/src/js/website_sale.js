/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.combineFilters = publicWidget.Widget.extend({
    selector: '.combo-filter',
    events: {
        'change': '_onChangeAttribute',
    },

    _onChangeAttribute: function (ev) {
        ev.preventDefault();
        console.log('_onChangeAttribute function called');

        // Update the URL with the selected combo_ids
        var form = $('#wsale_products_attributes_collapse').find('form');
        console.log('Form:', form);



        var url = new URL(window.location.href);
        var combos = []
        console.log($('.combo-filter:checked'))
        $('#products_grid_before .combo-filter:checked').each(function (index,element) {
            combos.push(element.value)

           $('<input>').attr({
            type: 'hidden',
            name: 'combo_products',
            value: element.value,
            }).appendTo(form);
        });console.log(combos)
        var combo_set = new Set(combos)
//        console.log('set',set)
        var combo_array = [...combo_set];
        console.log(combo_array)
//        console.log(aa)
        url.searchParams.set('combo_products', combo_array)
//        console.log(pp)


        window.location.href = url;

        console.log('input append to the form with value:', ev.target.value);
    },
});
