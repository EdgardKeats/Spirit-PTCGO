from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ab53ec89-20bd-5353-94f8-87c1b2bdef1b",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengarex.Name",
    display_name="Gengar ex",
    searchable_by=["Gengar ex", "Stage 2", "ex", "Gengarex"],
    subtypes=["Stage 2", "ex"],
    collector_number=154,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=94,
    abilities=[
        Ability(
            title="Fainting Spell",
            game_text="If this Pok\u00e9mon is Knocket Out by damage from an attack from your opponent's Pok\u00e9mon, flip a coin. If heads, the Attacking Pok\u00e9mon is Knocket Out.",
            effect=unimplemented,
        ),
        Attack(
            title="Chaotic Pain",
            game_text="Place 13 damage counters on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            effect=unimplemented,
        ),
    ],
)