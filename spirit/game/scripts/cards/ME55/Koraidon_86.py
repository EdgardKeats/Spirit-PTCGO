from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d7fd959e-a1c5-5bc0-ab73-690da228be03",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name",
    display_name="Koraidon",
    searchable_by=["Koraidon", "Basic", "Koraidon"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=1007,
    abilities=[
        Attack(
            title="Low Kick",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
        Attack(
            title="Collision Course",
            game_text="Discard 2 Fighting Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=unimplemented,
        ),
    ],
)