/** @odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { ConfirmPopup } from "@point_of_sale/app/utils/confirm_popup/confirm_popup";

export class TakeAwayButton extends ProductScreen {
    static template = "TakeAwayButton";
    setup() {
        this.pos = usePos();
    }

    async onClick() {
        // Make sure this.pos.popup is defined before using it
        if (this.pos.popup) {
            const { confirmed } = await this.pos.popup.add(ConfirmPopup, {
                title: _t("TakeAway Orders"),
                body: _t(
                    "Do you want to TakeAway this order?"
                ),
                confirmText: _t("Yes"),
                cancelText: _t("No"),
            });

            // Handle the result if needed
            if (confirmed) {
                // Do something if the user confirmed
            } else {
                // Do something if the user canceled
            }
        }
    }
}

ProductScreen.addControlButton({
    component: TakeAwayButton,
    position: ['before', 'OrderlineCustomerNoteButton'],
    // condition: function () {
    //     return this.pos.config.is_dine_in;
    // },
});
