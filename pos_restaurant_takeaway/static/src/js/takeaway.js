/** @odoo-module */
import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype, {
    setup(_defaultObj, options) {
        super.setup(...arguments);
        if (!this.pos.config.is_takeaway) {
            this.is_takeaway = false; // Set takeaway to true during setup
        }
    },
    export_for_printing() {
        return {
            ...super.export_for_printing(...arguments),
            is_takeaway: this.is_takeaway,
            token_number:this.token_number

        };
    },

    /**
     * Set takeaway value for the order.
     *
     * @param {boolean} isTakeaway - Indicates whether the order is for takeaway.
     */
    set_takeaway(isTakeaway) {
        this.is_takeaway = isTakeaway;
    },

    /**
     * Get the takeaway value for the order.
     *
     * @returns {boolean} - Indicates whether the order is for takeaway.
     */
    get_takeaway() {
        return this.is_takeaway;
    },
});
