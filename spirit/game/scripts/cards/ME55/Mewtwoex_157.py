from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="852c07df-f497-5181-8af3-50994581dcc5",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwoex.Name",
    display_name="Mewtwo ex",
    searchable_by=["Mewtwo ex", "Basic", "ex", "Mewtwoex"],
    subtypes=["Basic", "ex"],
    collector_number=157,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=150,
    abilities=[
        Attack(
            title="Photon Bullets",
            game_text="This attack does 50 damage to each of your opponent's Pok\u00e9mon ex. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Powers",
            game_text="During your next turn, this Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=230,
            effect=unimplemented,
        ),
    ],
)