from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="768d77c4-cadb-5dcf-8adc-463248e4cee1",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gholdengo.Name",
    display_name="Gholdengo",
    searchable_by=["Gholdengo", "Stage 1", "Gholdengo"],
    subtypes=["Stage 1"],
    collector_number=108,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    family_id=999,
    abilities=[
        Attack(
            title="Celebration",
            game_text="if you have exactly 30 cards in your hand, take 2 Prize cards. If you do, shuffle your hand into your deck.",
            cost={PokemonTypes.METAL: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Triple Smash",
            game_text="Flip 3 coins. This attack does 50 damage for each heads.",
            cost={PokemonTypes.METAL: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)