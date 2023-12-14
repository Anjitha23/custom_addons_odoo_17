/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";

export class TakeAwayButton extends ProductScreen {
    static template = "TakeAwayButton";

    setup() {
        this.pos = usePos();
    }

    async onClickPay() {
        // Navigate to the payment screen using the POS component
        this.pos.showScreen("PaymentScreen");
    }
}

ProductScreen.addControlButton({
    component: TakeAwayButton,
    position: ['before', 'OrderlineCustomerNoteButton'],
    // condition: function () {
    //     return this.pos.config.is_dine_in;
    // },
});
