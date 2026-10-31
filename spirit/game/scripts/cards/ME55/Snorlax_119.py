from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e5d0de0e-8635-552d-b41e-98c12d947bfa",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Good Sleep",
            game_text="If this Pok\u00e9mon remains Asleep during Pok\u00e9mon Checkup, heal all damage from this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Collapse",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)