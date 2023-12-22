/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";

export class TakeAwayButton extends ProductScreen {
    static template = "TakeAwayButton";

    setup() {
        this.pos = usePos();
        this.orm = useService("orm");
    }

    async onClick() {
        const order = this.pos.get_order();
        order.set_takeaway(true);
        order.takeawayButtonClicked = true;

        if (order.get_orderlines().length === 0) {
            alert("Cannot proceed with takeaway. Please add items to the order.");
            return;
        }

        const uid = order.uid;
        // Call the generate_token function on the server using useService
        const result = await this.orm.call("pos.config", "generate_token", [uid]);
        // Update the data property with the received token number
        this.pos.config.token_number = result
    }
}

// Register the component
ProductScreen.addControlButton({
    component: TakeAwayButton,
    condition: function () {
        return this.pos.config.is_takeaway;
    },
    position: ['before', 'OrderlineCustomerNoteButton']
});
