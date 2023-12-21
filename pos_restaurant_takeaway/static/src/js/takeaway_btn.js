/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";

export class TakeAwayButton extends ProductScreen {
    static template = "TakeAwayButton";

    setup() {
        try {
            this.pos = usePos();
            this.orm = useService("orm");
            console.log("TakeAwayButton setup:", this.pos, this.orm);
        } catch (error) {
            console.error("Error in TakeAwayButton setup:", error);
        }
    }

    async onClick() {
        try {
            console.log("TakeAwayButton onClick");

            // Set takeaway value on the order
            const order = this.pos.get_order();
            order.set_takeaway(true);
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

            // Update the order with the generated token number
            console.log("Generated Token:", result);
        } catch (error) {
            console.error("Error in TakeAwayButton onClick:", error);
            console.log("Error Response:", error.data); // Log the error response

            // Handle the error, e.g., show a user-friendly message
            // You may want to notify the user or take appropriate action
        }
    }
}

ProductScreen.addControlButton({
    component: TakeAwayButton,
    condition: function () {
        try {
            console.log("Condition Check:", this.pos.config.is_takeaway);
            return this.pos.config.is_takeaway;
        } catch (error) {
            console.error("Error in condition check:", error);
            return false; // or handle the error accordingly
        }
    },
    position: ['before', 'OrderlineCustomerNoteButton']
});
