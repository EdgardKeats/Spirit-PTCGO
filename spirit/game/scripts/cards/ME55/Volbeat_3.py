from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f7483bb3-097a-535d-bce1-3a8cb1cb5f42",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name",
    display_name="Volbeat",
    searchable_by=["Volbeat", "Basic", "Volbeat"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=313,
    abilities=[
        Attack(
            title="Luring Glow",
            game_text="Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Bug Buzz",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)