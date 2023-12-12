/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.combineFilters = publicWidget.Widget.extend({
    selector: '.form-check-input',
    events: {
        'change': '_onChangeAttribute',
    },

    _onChangeAttribute: function (ev) {
        ev.preventDefault();
        console.log('_onChangeAttribute function called');

        // Get the selected combo_ids from the checked checkboxes
        var combo_ids = [];
        $('.form-check-input:checked').each(function () {
            combo_ids.push($(this).val());
        });

        // Update the URL with the selected combo_ids
        var url = new URL(window.location.href);
        url.searchParams.set('combo_products', combo_ids.join(','));
        window.location.href = url;

        // Trigger a custom event or perform additional actions if needed
        // $(ev.currentTarget).closest("form").submit();
    },
});
