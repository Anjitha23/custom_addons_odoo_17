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
            // Set takeaway value on the order
            const order = this.pos.get_order();
            order.set_takeaway(true);
            order.set_token_number(true);
            order.takeawayButtonClicked = true;

            // Check if there are any order lines
            if (order.get_orderlines().length === 0) {
                // If no order lines, display an alert
                alert("Cannot proceed with takeaway. Please add items to the order.");
                return;
            }

            // Call the generate_token function on the server using useService
            const uid = order.uid;
            const result = await this.orm.call("pos.config", "generate_token", [uid]);
//            order.set_token_number(result.token_number);

    }
}

ProductScreen.addControlButton({
    component: TakeAwayButton,
    condition: function () {
            return this.pos.config.is_takeaway;
    },
    position: ['before', 'OrderlineCustomerNoteButton']
});
