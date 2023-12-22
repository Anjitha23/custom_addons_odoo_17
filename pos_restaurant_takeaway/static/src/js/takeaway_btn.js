/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";

export class TakeAwayButton extends ProductScreen {
    static template = "TakeAwayButton";

    setup() {
        this.pos = usePos();
        this.orm = useService("orm");

        // Ensure the existence of this.props.data
        if (!this.props.data) {
            this.props.data = {};
        }

        // Initialize data properties
        this.props.data.token_number = null;
    }

    async onClick() {
        const order = this.pos.get_order();
        order.set_takeaway(true);
        order.set_token_number(true);
        order.takeawayButtonClicked = true;

        if (order.get_orderlines().length === 0) {
            alert("Cannot proceed with takeaway. Please add items to the order.");
            return;
        }

        const uid = order.uid;

        // Call the generate_token function on the server using useService
        const result = await this.orm.call("pos.config", "generate_token", [uid]);

        // Update the data property with the received token number
                console.log('Token number received:', result);
        console.log('token',this.props.data.token_number);
        this.pos.config.token_number = result
        console.log('props',this.props)

        // Log for debugging

//        console.log('Updated props.data.token_number:', this.props.data.token_number);
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
