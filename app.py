
import streamlit as st
import pandas as pd
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Fulfillment Hub",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA = Path(__file__).parent / "data"

# ============================================================
# UI / UX STYLING
# ============================================================

st.markdown(
    """
    <style>
    /* ========================================================
       FULFILLMENT HUB - UI / UX SYSTEM
       ======================================================== */

    .block-container {
        max-width: 1480px;
        padding-top: 3rem;
        padding-bottom: 2rem;
        padding-left: 2.2rem;
        padding-right: 2.2rem;
    }

    /* ---------- Sidebar ---------- */
    [data-testid="stSidebar"] {
        border-right: 1px solid rgba(148, 163, 184, 0.18);
    }

    [data-testid="stSidebar"] .block-container {
        padding-top: 1.35rem;
    }

    .sidebar-brand {
        font-size: 1.08rem;
        font-weight: 750;
        color: #f8fafc;
        margin-bottom: 0.15rem;
    }

    .sidebar-subtitle {
        color: #94a3b8;
        font-size: 0.76rem;
        margin-bottom: 0.8rem;
    }

    /* ---------- Page header ---------- */
    .hero-title {
        font-size: 2rem;
        line-height: 1.25;
        font-weight: 750;
        letter-spacing: -0.02em;
        margin-top: 0.25rem;
        margin-bottom: 0.35rem;
        color: #f8fafc;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 0.92rem;
        line-height: 1.45;
        margin-bottom: 1.25rem;
    }

    .demo-badge {
        display: inline-block;
        border: 1px solid rgba(96, 165, 250, 0.28);
        background: rgba(59, 130, 246, 0.10);
        color: #93c5fd;
        border-radius: 999px;
        padding: 5px 10px;
        font-size: 0.72rem;
        font-weight: 650;
        margin-bottom: 1rem;
    }

    /* ---------- Section headings ---------- */
    .section-heading {
        font-size: 1.12rem;
        font-weight: 720;
        color: #f8fafc;
        margin: 0.55rem 0 0.45rem 0;
    }

    .section-description {
        color: #94a3b8;
        font-size: 0.80rem;
        line-height: 1.4;
        margin-top: 0;
        margin-bottom: 0.75rem;
    }

    /* ---------- KPI cards ---------- */
    .metric-card {
        border: 1px solid rgba(148, 163, 184, 0.20);
        border-radius: 14px;
        padding: 17px 18px;
        min-height: 112px;
        background: rgba(15, 23, 42, 0.32);
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    }

    .metric-label {
        color: #94a3b8;
        font-size: 0.73rem;
        font-weight: 650;
        text-transform: uppercase;
        letter-spacing: 0.045em;
    }

    .metric-value {
        color: #f8fafc;
        font-size: 1.95rem;
        font-weight: 760;
        margin-top: 7px;
        line-height: 1.05;
    }

    .metric-note {
        color: #94a3b8;
        font-size: 0.73rem;
        margin-top: 7px;
    }

    /* ---------- Action center ---------- */
    .action-card {
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 13px;
        padding: 15px 16px;
        min-height: 108px;
        background: rgba(15, 23, 42, 0.27);
    }

    .action-title {
        color: #f8fafc;
        font-size: 0.90rem;
        font-weight: 700;
    }

    .action-number {
        color: #f8fafc;
        font-size: 1.42rem;
        font-weight: 760;
        margin-top: 5px;
    }

    .action-text {
        color: #94a3b8;
        font-size: 0.75rem;
        line-height: 1.35;
        margin-top: 3px;
    }

    /* ---------- Page stat strip ---------- */
    .mini-stat {
        border: 1px solid rgba(148, 163, 184, 0.17);
        border-radius: 11px;
        padding: 11px 13px;
        background: rgba(15, 23, 42, 0.22);
    }

    .mini-stat-label {
        color: #94a3b8;
        font-size: 0.70rem;
        text-transform: uppercase;
        letter-spacing: 0.035em;
    }

    .mini-stat-value {
        color: #f8fafc;
        font-size: 1.25rem;
        font-weight: 730;
        margin-top: 2px;
    }

    /* ---------- Empty states ---------- */
    .empty-state {
        border: 1px dashed rgba(148, 163, 184, 0.25);
        border-radius: 12px;
        padding: 22px;
        text-align: center;
        color: #94a3b8;
        background: rgba(15, 23, 42, 0.16);
    }

    /* ---------- Streamlit controls ---------- */
    .stButton > button {
        border-radius: 9px;
        font-weight: 650;
    }

    div[data-baseweb="select"] > div {
        border-radius: 9px;
    }

    /* ---------- Tables ---------- */
    [data-testid="stDataFrame"] {
        border: 1px solid rgba(148, 163, 184, 0.16);
        border-radius: 10px;
        overflow: hidden;
    }

    /* ---------- Alerts ---------- */
    [data-testid="stAlert"] {
        border-radius: 10px;
    }

    /* ---------- Dividers ---------- */
    hr {
        margin: 1.25rem 0;
        border-color: rgba(148, 163, 184, 0.14);
    }

    /* ---------- Mobile / narrow screens ---------- */
    @media (max-width: 900px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 2rem;
        }

        .hero-title {
            font-size: 1.7rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    orders = pd.read_csv(DATA / "orders.csv")
    products = pd.read_csv(DATA / "products.csv")
    inventory = pd.read_csv(DATA / "inventory.csv")
    couriers = pd.read_csv(DATA / "couriers.csv")
    issues = pd.read_csv(DATA / "issues.csv")
    return orders, products, inventory, couriers, issues


orders, products, inventory, couriers, issues = load_data()

# ============================================================
# DERIVED FIELDS
# ============================================================

orders["pickup_deadline"] = pd.to_datetime(orders["pickup_deadline"])

demo_now = pd.Timestamp("2026-09-25 14:00")

open_statuses = [
    "Order Received",
    "Processed",
    "Picking",
    "Packing",
    "Packed",
    "Staging",
]

orders["priority_label"] = orders["priority"].map(
    {True: "Priority", False: "Regular"}
)

orders["is_open"] = orders["status"].isin(open_statuses)

orders["at_risk"] = (
    orders["is_open"]
    & (orders["pickup_deadline"] <= demo_now + pd.Timedelta(hours=1))
)

orders["overdue"] = (
    orders["is_open"]
    & (orders["pickup_deadline"] < demo_now)
)

inv = inventory.merge(
    products[
        ["sku", "product_name", "category", "variant", "reorder_level"]
    ],
    on="sku",
    how="left",
)

inv["main_available"] = inv["main_stock"] - inv["reserved"]

inv["available_stock"] = (
    inv["main_stock"]
    + inv["secondary_stock"]
    - inv["reserved"]
)

inv["transfer_required"] = inv["main_available"] < 0

inv["low_stock"] = inv["available_stock"] <= inv["reorder_level"]

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    '<div class="sidebar-brand">📦 Fulfillment Hub</div>',
    unsafe_allow_html=True,
)
st.sidebar.markdown(
    '<div class="sidebar-subtitle">XYZ operational control center</div>',
    unsafe_allow_html=True,
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate",
    [
        "Dashboard",
        "Orders",
        "Inventory",
        "Exceptions",
        "Shipping & Pickup",
    ],
)

st.sidebar.divider()

st.sidebar.caption("Demo environment")
st.sidebar.info("Sample data only • 250 orders/day")

# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.markdown(
        '<div class="hero-title">Fulfillment Hub</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-subtitle">'
        'What needs attention right now? • Demo date: 25 Sep 2026'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="demo-badge">DEMO ENVIRONMENT • 250 ORDERS / DAY</div>',
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------------

    a, b, c, d = st.columns(4)

    metrics = [
        (
            "Total orders",
            f"{len(orders):,}",
            "Orders in today's sample",
        ),
        (
            "Priority orders",
            f"{int((orders.priority & orders.is_open).sum()):,}",
            "Need same-day handling",
        ),
        (
            "Orders at risk",
            f"{int(orders.at_risk.sum()):,}",
            "Within the pickup-risk window",
        ),
        (
            "Open issues",
            f"{int((issues.resolution_status == 'Open').sum()):,}",
            "Exceptions requiring attention",
        ),
    ]

    for col, (label, value, note) in zip([a, b, c, d], metrics):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{value}</div>
                    <div class="metric-note">{note}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()

    # --------------------------------------------------------
    # ACTION CENTER
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-heading">⚠️ What needs attention right now?</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-description">'
        'Start with the work most likely to cause a fulfillment delay.'
        '</div>',
        unsafe_allow_html=True,
    )

    transfer_count = int(inv.transfer_required.sum())
    priority_count = int((orders.priority & orders.is_open).sum())
    issue_count = int((issues.resolution_status == "Open").sum())

    ac1, ac2, ac3 = st.columns(3)

    with ac1:
        st.markdown(
            f"""
            <div class="action-card">
                <div class="action-title">📦 Inventory transfers</div>
                <div class="action-number">{transfer_count}</div>
                <div class="action-text">
                    SKU checks requiring transfer or stock verification.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with ac2:
        st.markdown(
            f"""
            <div class="action-card">
                <div class="action-title">🚨 Priority orders</div>
                <div class="action-number">{priority_count}</div>
                <div class="action-text">
                    Priority orders still moving through fulfillment.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with ac3:
        st.markdown(
            f"""
            <div class="action-card">
                <div class="action-title">⚠️ Open exceptions</div>
                <div class="action-number">{issue_count}</div>
                <div class="action-text">
                    Operational issues that need follow-up.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    # --------------------------------------------------------
    # PIPELINE
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-heading">Fulfillment pipeline</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-description">'
        'Current order distribution across the fulfillment stages. '
        'Use this view to spot where work is accumulating.'
        '</div>',
        unsafe_allow_html=True,
    )

    # Explicit categorical order prevents the chart from alphabetically
    # reordering the fulfillment stages.
    stage_order = [
        "Order Received",
        "Processed",
        "Picking",
        "Packing",
        "Packed",
        "Staging",
        "Shipped",
        "Delivered",
    ]

    pipeline = (
        orders.groupby("status")
        .size()
        .reindex(stage_order, fill_value=0)
        .rename_axis("Stage")
        .reset_index(name="Orders")
    )

    pipeline["Stage"] = pd.Categorical(
        pipeline["Stage"],
        categories=stage_order,
        ordered=True,
    )

    pipeline = pipeline.sort_values("Stage")

    import altair as alt

    pipeline_chart = (
        alt.Chart(pipeline)
        .mark_bar()
        .encode(
            x=alt.X(
                "Stage:N",
                sort=stage_order,
                title=None,
                axis=alt.Axis(labelAngle=-35),
            ),
            y=alt.Y(
                "Orders:Q",
                title="Orders",
                scale=alt.Scale(zero=True),
            ),
            tooltip=[
                alt.Tooltip("Stage:N", title="Stage"),
                alt.Tooltip("Orders:Q", title="Orders"),
            ],
        )
        .properties(height=300)
    )

    st.altair_chart(
        pipeline_chart,
        use_container_width=True,
    )

    st.divider()

    # --------------------------------------------------------
    # PRIORITY + INVENTORY
    # --------------------------------------------------------

    left, right = st.columns([1.35, 1])

    with left:

        st.markdown(
            '<div class="section-heading">'
            '🚨 Priority orders requiring attention'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-description">'
            'Prioritized by overdue status and pickup deadline.'
            '</div>',
            unsafe_allow_html=True,
        )

        watch = (
            orders[(orders.priority) & (orders.is_open)]
            .sort_values(
                ["overdue", "pickup_deadline"],
                ascending=[False, True],
            )
            .head(12)
            .copy()
        )

        watch["Action"] = watch.apply(
            lambda r:
            "🔴 Act now"
            if r.overdue
            else (
                "🟠 Protect SLA"
                if r.at_risk
                else "Process"
            ),
            axis=1,
        )

        if watch.empty:
            st.markdown(
                '<div class="empty-state">No open priority orders require attention.</div>',
                unsafe_allow_html=True,
            )
        else:
            st.dataframe(
                watch[
                    [
                        "order_id",
                        "status",
                        "courier",
                        "pickup_deadline",
                        "at_risk",
                        "Action",
                    ]
                ],
                use_container_width=True,
                hide_index=True,
            )

    with right:

        st.markdown(
            '<div class="section-heading">📦 Inventory alerts</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-description">'
            'Stock conditions that may affect picking.'
            '</div>',
            unsafe_allow_html=True,
        )

        alerts = inv[
            inv.low_stock | inv.transfer_required
        ].head(12)

        if alerts.empty:
            st.markdown(
                '<div class="empty-state">No inventory alerts currently require attention.</div>',
                unsafe_allow_html=True,
            )
        else:
            st.dataframe(
                alerts[
                    [
                        "sku",
                        "product_name",
                        "main_available",
                        "secondary_stock",
                        "transfer_required",
                        "low_stock",
                    ]
                ],
                use_container_width=True,
                hide_index=True,
            )

# ============================================================
# ORDERS
# ============================================================

elif page == "Orders":

    st.markdown(
        '<div class="hero-title">📋 Orders</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-subtitle">'
        "Priority work is surfaced before regular work."
        "</div>",
        unsafe_allow_html=True,
    )

    f1, f2, f3 = st.columns(3)

    pf = f1.selectbox(
        "Priority",
        ["All", "Priority", "Regular"],
    )

    sf = f2.selectbox(
        "Status",
        ["All"] + sorted(orders.status.unique()),
    )

    cf = f3.selectbox(
        "Courier",
        ["All"] + sorted(orders.courier.unique()),
    )

    st.markdown(
        '<div class="section-heading">Order workload</div>',
        unsafe_allow_html=True,
    )

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.metric("Orders", len(orders))

    with s2:
        st.metric("Priority", int((orders.priority & orders.is_open).sum()))

    with s3:
        st.metric("At risk", int(orders.at_risk.sum()))

    with s4:
        st.metric("Overdue", int(orders.overdue.sum()))

    st.markdown(
        '<div class="section-description">'
        'Use the filters above to narrow the queue. Urgent work is sorted first.'
        '</div>',
        unsafe_allow_html=True,
    )

    q = orders.copy()

    if pf != "All":
        q = q[q.priority_label == pf]

    if sf != "All":
        q = q[q.status == sf]

    if cf != "All":
        q = q[q.courier == cf]

    q = q.sort_values(
        ["overdue", "priority", "pickup_deadline"],
        ascending=[False, False, True],
    )

    q["Action"] = q.apply(
        lambda r:
        "🔴 Act before pickup"
        if r.overdue
        else (
            "🟠 Protect SLA"
            if r.priority and r.at_risk
            else "Process normally"
        ),
        axis=1,
    )

    st.dataframe(
        q[
            [
                "order_id",
                "priority_label",
                "sku",
                "quantity",
                "status",
                "courier",
                "pickup_deadline",
                "at_risk",
                "Action",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )

# ============================================================
# INVENTORY
# ============================================================

elif page == "Inventory":

    st.markdown(
        '<div class="hero-title">📦 Inventory</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-subtitle">'
        "Orders ship from the main warehouse; secondary stock may require transfer."
        "</div>",
        unsafe_allow_html=True,
    )

    a, b, c = st.columns(3)

    a.metric("SKUs", len(inv))
    b.metric("Low-stock SKUs", int(inv.low_stock.sum()))
    c.metric("Transfer checks", int(inv.transfer_required.sum()))

    st.markdown(
        '<div class="section-description">'
        'Main available = main warehouse stock minus reserved stock. '
        'Transfer required means the main warehouse cannot cover reserved demand.'
        '</div>',
        unsafe_allow_html=True,
    )

    st.divider()

    view = st.radio(
        "View",
        ["All", "Low stock", "Transfer required"],
        horizontal=True,
    )

    x = inv.copy()

    if view == "Low stock":
        x = x[x.low_stock]

    if view == "Transfer required":
        x = x[x.transfer_required]

    if x.empty:
        st.markdown(
            '<div class="empty-state">No SKUs match this inventory view.</div>',
            unsafe_allow_html=True,
        )
    else:
        st.dataframe(
            x[
                [
                    "sku",
                    "product_name",
                    "variant",
                    "main_stock",
                    "secondary_stock",
                    "reserved",
                    "main_available",
                    "available_stock",
                    "reorder_level",
                    "transfer_required",
                    "low_stock",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )

# ============================================================
# EXCEPTIONS
# ============================================================

elif page == "Exceptions":

    st.markdown(
        '<div class="hero-title">⚠️ Exceptions</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-subtitle">'
        "One action list for problems that could otherwise be forgotten."
        "</div>",
        unsafe_allow_html=True,
    )

    sev = st.multiselect(
        "Severity",
        sorted(issues.severity.unique()),
        default=sorted(issues.severity.unique()),
    )

    typ = st.multiselect(
        "Issue type",
        sorted(issues.issue_type.unique()),
        default=sorted(issues.issue_type.unique()),
    )

    st.markdown(
        '<div class="section-heading">Exception workload</div>',
        unsafe_allow_html=True,
    )

    e1, e2, e3, e4 = st.columns(4)

    with e1:
        st.metric("Issues shown", len(issues[issues.severity.isin(sev) & issues.issue_type.isin(typ)]))

    with e2:
        st.metric("High severity", int((issues.severity == "High").sum()))

    with e3:
        st.metric("Inventory", int((issues.issue_type == "Inventory").sum()))

    with e4:
        st.metric("Pickup / SLA", int(issues.issue_type.isin(["Pickup", "SLA"]).sum()))

    st.markdown(
        '<div class="section-description">'
        'Use the filters to isolate the exceptions that need immediate follow-up.'
        '</div>',
        unsafe_allow_html=True,
    )

    x = issues[
        issues.severity.isin(sev)
        & issues.issue_type.isin(typ)
    ].copy()

    action_map = {
        "Inventory": "Transfer or verify stock",
        "Picking": "Verify SKU/variant before packing",
        "Pickup": "Confirm box location and courier pickup",
        "SLA": "Prioritize order and protect same-day pickup",
    }

    x["Recommended action"] = x.issue_type.map(action_map)

    if x.empty:
        st.markdown(
            '<div class="empty-state">No exceptions match the selected filters.</div>',
            unsafe_allow_html=True,
        )
    else:
        st.dataframe(
            x[
                [
                    "issue_id",
                    "reference_id",
                    "issue_type",
                    "severity",
                    "description",
                    "Recommended action",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )

# ============================================================
# SHIPPING & PICKUP
# ============================================================

elif page == "Shipping & Pickup":

    st.markdown(
        '<div class="hero-title">🚚 Shipping & Pickup</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-subtitle">'
        "Monitor packed/staged orders and courier pickup risk."
        "</div>",
        unsafe_allow_html=True,
    )

    ship1, ship2, ship3, ship4 = st.columns(4)

    with ship1:
        st.metric("Orders", len(orders))

    with ship2:
        st.metric("Couriers", orders["courier"].nunique())

    with ship3:
        st.metric("At risk", int(orders.at_risk.sum()))

    with ship4:
        st.metric("Overdue", int(orders.overdue.sum()))

    st.markdown(
        '<div class="section-heading">Courier workload</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-description">'
        'Compare courier workload and identify pickup pressure before cutoff.'
        '</div>',
        unsafe_allow_html=True,
    )

    summary = (
        orders.groupby("courier")
        .agg(
            Orders=("order_id", "count"),
            Priority=("priority", "sum"),
            At_Risk=("at_risk", "sum"),
            Overdue=("overdue", "sum"),
        )
        .reset_index()
    )

    summary = (
        summary
        .merge(
            couriers[
                [
                    "courier_name",
                    "service_level",
                    "base_cost",
                    "pickup_cutoff",
                ]
            ],
            left_on="courier",
            right_on="courier_name",
            how="left",
        )
        .drop(columns="courier_name")
    )

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown(
        '<div class="section-heading">Pickup watch</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-description">'
        'Packed and staged orders are shown first so pickup deadlines are easier to protect.'
        '</div>',
        unsafe_allow_html=True,
    )

    p = (
        orders[
            orders.status.isin(["Packed", "Staging"])
        ]
        .sort_values("pickup_deadline")
    )

    st.dataframe(
        p[
            [
                "order_id",
                "priority_label",
                "status",
                "courier",
                "pickup_deadline",
                "at_risk",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Fulfillment Hub • XYZ operational control center • Demo data only"
)
