from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a7d718cf-5adb-5a65-bfbf-08e51c34783a",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachuex.Name",
    display_name="Pikachu ex",
    searchable_by=["Pikachu ex", "Basic", "ex", "Pikachuex"],
    subtypes=["Basic", "ex"],
    collector_number=54,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Zip-Zap Frenzy",
            game_text="You may attach any number of Basic Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Thunder",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)