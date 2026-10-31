from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

async def fetch_and_hide(ctx):
    """Opponent reveals their hand, you put an item card you find there on the bottom of your opponent's deck."""
    selected_item_card = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)


card = PokemonCardDef(
    guid="315576e4-1a7a-5c30-be3b-d723c155ab44",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Fetch and Hide",
            game_text="Your opponent reveals their hand, and you put an Item card you find there on the bottom of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)