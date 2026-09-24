import streamlit as st
import pandas as pd
from pathlib import Path
from difflib import get_close_matches


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="IPL Player Recommendation System",
    page_icon="🏏",
    layout="wide"
)


# ============================================================
# LOAD COSINE SIMILARITY DATA
# ============================================================

@st.cache_data
def load_similarity_data():

    # app/app.py
    #     ↓
    # app/
    #     ↓
    # Data-science/
    #
    # Therefore, go one level up from app/

    project_root = Path(__file__).resolve().parent.parent

    file_path = (
        project_root
        / "data"
        / "cosine_similarity.parquet"
    )

    df = pd.read_parquet(file_path)

    return df


# ============================================================
# LOAD DATA WITH ERROR HANDLING
# ============================================================

try:

    cosine_similarity_df = load_similarity_data()

except Exception as e:

    st.error(
        "❌ Unable to load the cosine similarity data."
    )

    st.write("Error details:")

    st.code(str(e))

    st.stop()


# ============================================================
# CLEAN PLAYER NAMES
# ============================================================

cosine_similarity_df.index = (
    cosine_similarity_df.index
    .astype(str)
    .str.strip()
)

cosine_similarity_df.columns = (
    cosine_similarity_df.columns
    .astype(str)
    .str.strip()
)


# List of players

players = cosine_similarity_df.index.tolist()


# ============================================================
# FUZZY PLAYER SEARCH
# ============================================================

def find_player(user_input, players):

    """
    Find the closest player name using:

    1. Exact match
    2. Partial match
    3. Fuzzy match
    """

    user_input = user_input.strip()

    if not user_input:

        return None, []


    # --------------------------------------------------------
    # 1. EXACT MATCH
    # --------------------------------------------------------

    exact_matches = [
        player
        for player in players
        if player.lower() == user_input.lower()
    ]

    if exact_matches:

        return exact_matches[0], exact_matches


    # --------------------------------------------------------
    # 2. PARTIAL MATCH
    # --------------------------------------------------------

    partial_matches = [
        player
        for player in players
        if user_input.lower() in player.lower()
    ]

    if partial_matches:

        return partial_matches[0], partial_matches


    # --------------------------------------------------------
    # 3. FUZZY MATCH
    # --------------------------------------------------------

    fuzzy_matches = get_close_matches(
        user_input,
        players,
        n=5,
        cutoff=0.4
    )

    if fuzzy_matches:

        return fuzzy_matches[0], fuzzy_matches


    # --------------------------------------------------------
    # NO MATCH
    # --------------------------------------------------------

    return None, []


# ============================================================
# RECOMMENDATION FUNCTION
# ============================================================

def recommend_players(
    player,
    number_of_recommendations=5
):

    """
    Return players with the highest cosine similarity
    to the selected player.
    """

    # Get similarity values for selected player

    similarities = cosine_similarity_df.loc[player]


    # Remove the selected player itself

    similarities = similarities.drop(
        player,
        errors="ignore"
    )


    # Sort from highest similarity to lowest

    recommendations = (
        similarities
        .sort_values(ascending=False)
        .head(number_of_recommendations)
    )


    # Convert Series to DataFrame

    recommendations = (
        recommendations
        .reset_index()
    )


    # Rename columns

    recommendations.columns = [
        "Player",
        "Similarity"
    ]


    # --------------------------------------------------------
    # Convert cosine similarity to percentage
    # --------------------------------------------------------

    recommendations["Similarity"] = (
        recommendations["Similarity"] * 100
    ).round(2)


    # Add percentage symbol

    recommendations["Similarity"] = (
        recommendations["Similarity"]
        .astype(str)
        + "%"
    )


    # Return only required columns

    recommendations = recommendations[
        [
            "Player",
            "Similarity"
        ]
    ]


    return recommendations


# ============================================================
# APPLICATION TITLE
# ============================================================

st.title(
    "🏏 IPL Player Recommendation System"
)


st.markdown(
    """
    Find IPL players with similar statistical profiles
    using **Cosine Similarity**.
    """
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header(
    "🔍 Player Search"
)


# ------------------------------------------------------------
# Player input
# ------------------------------------------------------------

user_input = st.sidebar.text_input(
    "Enter player name",
    placeholder="Example: Virat Kohli"
)


# ------------------------------------------------------------
# Number of recommendations
# ------------------------------------------------------------

number_of_recommendations = st.sidebar.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5
)


# ============================================================
# PLAYER SEARCH
# ============================================================

selected_player = None

matches = []


if user_input:

    selected_player, matches = find_player(
        user_input,
        players
    )


# ============================================================
# DISPLAY MATCHES
# ============================================================

if user_input:

    if selected_player:

        # ----------------------------------------------------
        # Exact match
        # ----------------------------------------------------

        if (
            len(matches) == 1
            and matches[0].lower()
            == user_input.strip().lower()
        ):

            st.sidebar.success(
                f"✓ {selected_player}"
            )


        # ----------------------------------------------------
        # Multiple matches
        # ----------------------------------------------------

        elif len(matches) > 1:

            st.sidebar.info(
                "Multiple players found."
            )

            selected_player = st.sidebar.selectbox(
                "Select player",
                matches
            )


        # ----------------------------------------------------
        # Fuzzy match
        # ----------------------------------------------------

        else:

            st.sidebar.info(
                f"Did you mean: {selected_player}?"
            )

            selected_player = st.sidebar.selectbox(
                "Select player",
                matches
            )


    else:

        st.sidebar.error(
            "❌ No matching player found."
        )


# ============================================================
# MAIN APPLICATION
# ============================================================

if selected_player:

    # --------------------------------------------------------
    # Selected player
    # --------------------------------------------------------

    st.subheader(
        "Selected Player"
    )

    st.info(
        f"🏏 **{selected_player}**"
    )


    # --------------------------------------------------------
    # Get recommendations automatically
    # --------------------------------------------------------

    recommendations = recommend_players(
        selected_player,
        number_of_recommendations
    )


    # --------------------------------------------------------
    # Display recommendations
    # --------------------------------------------------------

    st.subheader(
        "🎯 Similar Players"
    )


    if recommendations.empty:

        st.warning(
            "No similar players found."
        )

    else:

        st.dataframe(
            recommendations,
            use_container_width=True,
            hide_index=True
        )


# ============================================================
# INITIAL MESSAGE
# ============================================================

else:

    st.info(
        "👈 Enter a player name in the sidebar "
        "to find similar players."
    )


# ============================================================
# COSINE SIMILARITY MATRIX
# ============================================================

with st.expander(
    "📊 View Cosine Similarity Matrix"
):

    st.dataframe(
        cosine_similarity_df,
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Recommendation method: Cosine Similarity | "
    "IPL Player Recommendation System"
)