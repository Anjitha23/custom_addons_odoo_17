/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";

export class TakeAwayButton extends ProductScreen {
    static template = "TakeAwayButton";

    setup() {
        this.pos = usePos();

    }

    onClick() {
        console.log(this.pos.get_order())
        // Toggle the value when the button is clicked
        // Set takeaway value on the order
        this.pos.get_order().set_takeaway(true);
        this.pos.get_order().takeawayButtonClicked = true;


        // Log the current value (you can remove this in production)
        console.log("Button Value:", this.isButtonEnabled);
    }

}

ProductScreen.addControlButton({

    component: TakeAwayButton,
    condition: function () {
            console.log("jkjkjjkj",this.pos)
            return this.pos.config.is_takeaway;
        },
    position: ['before', 'OrderlineCustomerNoteButton']
});